document.addEventListener("DOMContentLoaded", () => {
  const activitiesList = document.getElementById("activities-list");
  const activitySelect = document.getElementById("activity");
  const signupForm = document.getElementById("signup-form");
  const messageDiv = document.getElementById("message");

  // Function to fetch activities from API
  async function fetchActivities() {
    try {
      const response = await fetch("/activities");
      const activities = await response.json();

      // Clear loading message and reset activity options
      activitiesList.innerHTML = "";
      activitySelect.innerHTML = '<option value="">-- Select an activity --</option>';

      // Populate activities list
      Object.entries(activities).forEach(([name, details]) => {
        const activityCard = document.createElement("div");
        activityCard.className = "activity-card";

        const spotsLeft = details.max_participants - details.participants.length;

        activityCard.innerHTML = `
          <h4>${name}</h4>
          <p>${details.description}</p>
          <p><strong>Schedule:</strong> ${details.schedule}</p>
          <p><strong>Availability:</strong> ${spotsLeft} spots left</p>
          <div class="participants">
            <strong>Participants</strong>
            <div class="participants-list-container"></div>
          </div>
        `;

        const participantsContainer = activityCard.querySelector('.participants-list-container');

        if (details.participants.length > 0) {
          const participantsList = document.createElement('ul');
          participantsList.className = 'participants-list';

          details.participants.forEach((participant) => {
            const listItem = document.createElement('li');
            listItem.className = 'participant-item';

            const label = document.createElement('span');
            label.textContent = participant;
            label.className = 'participant-name';

            const deleteButton = document.createElement('button');
            deleteButton.type = 'button';
            deleteButton.className = 'participant-delete';
            deleteButton.title = `Remove ${participant}`;
            deleteButton.textContent = '✕';

            deleteButton.addEventListener('click', async () => {
              try {
                const deleteResponse = await fetch(
                  `/activities/${encodeURIComponent(name)}/participants?email=${encodeURIComponent(participant)}`,
                  { method: 'DELETE' }
                );

                const deleteResult = await deleteResponse.json();

                if (deleteResponse.ok) {
                  messageDiv.textContent = deleteResult.message;
                  messageDiv.className = 'success';
                  fetchActivities();
                } else {
                  messageDiv.textContent = deleteResult.detail || 'Failed to remove participant';
                  messageDiv.className = 'error';
                }

                messageDiv.classList.remove('hidden');
                setTimeout(() => messageDiv.classList.add('hidden'), 5000);
              } catch (error) {
                messageDiv.textContent = 'Failed to remove participant. Please try again.';
                messageDiv.className = 'error';
                messageDiv.classList.remove('hidden');
                console.error('Error removing participant:', error);
              }
            });

            listItem.appendChild(label);
            listItem.appendChild(deleteButton);
            participantsList.appendChild(listItem);
          });

          participantsContainer.appendChild(participantsList);
        } else {
          participantsContainer.innerHTML = '<p class="no-participants">No participants yet.</p>';
        }

        activitiesList.appendChild(activityCard);

        // Add option to select dropdown
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        activitySelect.appendChild(option);
      });
    } catch (error) {
      activitiesList.innerHTML = "<p>Failed to load activities. Please try again later.</p>";
      console.error("Error fetching activities:", error);
    }
  }

  // Handle form submission
  signupForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const activity = document.getElementById("activity").value;

    try {
      const response = await fetch(
        `/activities/${encodeURIComponent(activity)}/signup?email=${encodeURIComponent(email)}`,
        {
          method: "POST",
        }
      );

      const result = await response.json();

      if (response.ok) {
        messageDiv.textContent = result.message;
        messageDiv.className = "success";
        signupForm.reset();
        fetchActivities();
      } else {
        messageDiv.textContent = result.detail || "An error occurred";
        messageDiv.className = "error";
      }

      messageDiv.classList.remove("hidden");

      // Hide message after 5 seconds
      setTimeout(() => {
        messageDiv.classList.add("hidden");
      }, 5000);
    } catch (error) {
      messageDiv.textContent = "Failed to sign up. Please try again.";
      messageDiv.className = "error";
      messageDiv.classList.remove("hidden");
      console.error("Error signing up:", error);
    }
  });

  // Initialize app
  fetchActivities();
});
