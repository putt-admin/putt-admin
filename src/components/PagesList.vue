<template>
  <div class="row">
    <div class="col-6">
      <div class="card">
        <div class="card-header">
          <h4>App Menu</h4>
          <div class="card-header-action"></div>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-striped" id="sortable-table">
              <thead>
                <tr>
                  <th class="text-center">
                    <i class="fas fa-th"></i>
                  </th>
                  <th>Menu</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>
                    <div class="sort-handler">
                      <i class="fas fa-th"></i>
                    </div>
                  </td>
                  <td>Create a mobile app</td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>
                    <div class="sort-handler">
                      <i class="fas fa-th"></i>
                    </div>
                  </td>
                  <td>Redesign homepage</td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
    <div class="col-6">
      <div class="card">
        <div class="card-header">
          <h4>All Pages</h4>
          <div class="card-header-action"></div>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-striped" id="sortable-table">
              <thead>
                <tr>
                  <th>Page</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Page new 1</td>
                  <td><a href="#" class="btn btn-secondary">Detail</a></td>
                </tr>
                <tr>
                  <td>Page new 2</td>
                  <td><a href="#" class="btn btn-primary">Detail</a></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
